import java.util.*

class Solution {
    fun solution(priorities: IntArray, location: Int): Int {
        var answer = 0
        var cursor = location
        val deque = ArrayDeque<Int>()
        for(priority in priorities){
            deque.offer(priority)
        }
        var maxValIdx = 0
        priorities.sortDescending()
        while(deque.isNotEmpty()){
            cursor = (cursor - 1 + deque.count()) % deque.count()
            val popped = deque.poll()
            if(priorities[maxValIdx] > popped){
                deque.offer(popped)
                continue
            }
            maxValIdx += 1
            answer += 1
            if(cursor == deque.count()) break
        }      
        return answer
        
    }        
}