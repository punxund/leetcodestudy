#https://leetcode.com/problems/merge-nodes-in-between-zeros/
#2022-11-12 Hongsik Kim

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #새로운 링크드리스트 생성
        linkedlist = ListNode()
        #링크드리스트의 헤드 지정
        merged_head = linkedlist
        #처음노드 필요없으니 다음노드로 이동
        head = head.next
        
        
        #다음 헤드가 없을때 까지 계속
        while head.next != None :
            #헤드 밸류가 0이 아니면 새로운 링크드리스트 밸류에 더하기 
            if head.val != 0 :
                linkedlist.val += head.val
            #헤드 밸류가 0이면 새로운 링크드리스트의 다음 노드 생성
            else :                
                linkedlist.next = ListNode()
                linkedlist = linkedlist.next
            #헤드 다음 노드로 이동
            head = head.next

        return merged_head