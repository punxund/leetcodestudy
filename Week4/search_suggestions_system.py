# https://leetcode.com/problems/search-suggestions-system/
# 2022-12-02 Hongsik Kim

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # products sorted lexicographically
        products.sort() # O(nlogn)

        # from the sorted product list, get 3 products that have word as prefix.
        def search(word):
            product_list = []
            counter = 0
            for i in products:
                if counter < 3 and word == i[:len(word)]:
                    product_list.append(i)
                    counter += 1
            return product_list

        # Search for products by adding letters of searchWord one by one.
        suggested_product = []
        for i in range(len(searchWord)): # time complexity : O(n*m) n is length of products and m is length of searchWord
            suggest = search(searchWord[:i+1])
            suggested_product.append(suggest)
        
        return suggested_product