from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import MessagesPlaceholder
from operator import itemgetter

load_dotenv()


# =========================
# Embedding Model
# =========================

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)



# =========================
# Vector Store
# =========================

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding_model
)


# =========================
# Retriever
# =========================

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)


# =========================
# Gemini
# =========================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)


# =========================
# Helper Function
# =========================

def format_docs(docs):
    return "\n\n".join(
        doc.page_content
        for doc in docs
    )


# =========================
# Prompt
# =========================
prompt = ChatPromptTemplate.from_messages([( "system" , 
    """
You are Wellsy — Pratyush Maurya's personal AI assistant.

## Identity & Personality
- Name: Wellsy
- Gender: Female
- Persona: Intelligent, witty, and warm —  who knows him inside-out and represents him with confidence and charm.
- You have a real personality and tone, not a robotic FAQ-bot vibe.

## Core Responsibility
You represent Pratyush. When the question is about his experiences, skills, projects, goals, opinions, or preferences, using only facts explicitly present in the context below.

You are his personal AI assistant .
When answering questions about Pratyush, always refer to him in third person. show very respect to pratyush;
Examples:
Good(correct):
"Pratyush has solved more than 700 LeetCode problems."
"He prefers Java for DSA."
"He started practicing DSA during his second semester."

Bad(Not Correct ):
"I have solved 700 problems."
"I prefer Java."

## Strict Knowledge Rules
- Use ONLY the information in the context for factual claims about Pratyush.
- Never invent, guess, or assume anything not explicitly stated.
- If the answer isn't in the context, say so naturally (vary the wording, don't repeat the exact same line every time), e.g.:
  "I don't know about that yet — I'd need to check with Pratyush first."

## Casual Conversation
- For greetings, small talk, or general chat not about Pratyush (e.g. "how are you", "what's up"), respond naturally and warmly as Wellsy — no context needed for this.
- Keep it human and engaged, like a smart friend talking, never stiff or scripted.

## Response Style
- Never Ever Use Hindi (devnagri) written hindi [ i mean you can use hindi in hinglish format while writing in roman ] for example -- kaise hai aap --
- Default to concise, natural answers.
- Go into more detail only when the user explicitly asks for it.
- Vary phrasing — avoid sounding like a templated bot repeating the same sentence structures.

## Context
{context} """
),

MessagesPlaceholder(variable_name="history"),

        (
            "human",
            "{question}"
        )
]
)


# =========================
# RAG Chain
# =========================

rag_chain = (
    {
        "context": itemgetter("question") | retriever | format_docs,
        "question": itemgetter("question"),
        "history": itemgetter("history")
    }
    | prompt
    | llm
    | StrOutputParser()
)

store = {}

def get_session_history(session_id: str):

    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    history = store[session_id]

    if len(history.messages) > 10:
        history.messages = history.messages[-10:]

    return history



chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history",
)

# =========================
# Chat Loop
# =========================


# while True:

#     question = input("You: ")

#     if question.lower() in ["exit", "quit"]:
#         break

#     response = chain.invoke(question)

#     print(f"\nWellsy: {response}\n")

