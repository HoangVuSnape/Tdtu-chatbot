from typing import List, Dict, Optional
from langchain.docstore.document import Document
from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv
import os
from pathlib import Path
import json
import langdetect

load_dotenv(Path("../.env"))
os.environ["TAVILY_API_KEY"] = os.getenv('tavily_api')

class WebSearching:
    def __init__(self, max_result: int = 5, search_depth: str = "basic"):
        self.searcher = TavilySearchResults(
            max_results=  max_result,
            search_depth= search_depth,
            include_answer=True,
            include_raw_content=True,
            include_images=False,
        )

    # def search(self, query: str, ) -> List[Document]:
    #     response = self.searcher.invoke({"query": query})
    #     docs = []
    #     for result in response:
    #         docs.append(result['url'] + "\n" + result['content'])
    #     return docs
    def search(self, query: str) -> List[str]:
        response = self.searcher.invoke({"query": query})
        docs = []
        for result in response:
            content = result['content']
            # Lọc kết quả chỉ lấy nội dung bằng tiếng Việt
            if langdetect.detect(content) == 'vi':
                docs.append(result['url'] + "\n" + content)
        return docs
    
if __name__ == "__main__":   

    searching = WebSearching()
    query = "Thủ tướng Nguyễn Minh Chính?"
    docs = searching.search(query)
    print(len(docs))
    for i in docs:
        print(i)
        print("----------------------")