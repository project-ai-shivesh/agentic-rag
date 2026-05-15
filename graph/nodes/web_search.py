import os
from typing import Any, TypedDict, Dict

from langchain_core import documents
from langchain_core.documents import Document
from langchain_tavily import TavilySearch
from graph.state import GraphState
from dotenv import load_dotenv
load_dotenv()


web_search_tool = TavilySearch(max_results=3)

def web_search(state: GraphState) -> Dict[str,Any]:
    print("------- Searching web------")
    question = state["question"]
    docs = state["documents"]

    tavily_results = web_search_tool.invoke({"query":question})
    joined_tavily_results = "\n".join(
        [tavily_result["content"] for tavily_result in tavily_results["results"]]
    )

    web_results = Document(page_content=joined_tavily_results)

    if docs is not None:
        docs.append(web_results)
    else:
        docs = [web_results]

    return {"documents": docs, "question": question}

if __name__ == "__main__":
    web_search(state={"question":"agent memory", "documents": None})
