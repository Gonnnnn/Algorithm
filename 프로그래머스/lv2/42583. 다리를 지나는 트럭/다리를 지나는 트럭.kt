import java.util.*

class Solution {
    fun solution(bridge_length: Int, weight: Int, truck_weights: IntArray): Int {
        var answer = 0
        val deque = ArrayDeque<Int>()
        for(i in 0 until bridge_length){
            deque.offer(0)
        }
        var onBridge = 0
        var idx = 0
        while(idx < truck_weights.count() || onBridge != 0){
            if(deque.isNotEmpty()){
                val popped = deque.poll()
                onBridge -= popped
                
            }
            if(idx < truck_weights.count() && truck_weights[idx] + onBridge <= weight){
                deque.offer(truck_weights[idx])
                onBridge += truck_weights[idx]
                idx += 1
            }else if(deque.count() < bridge_length){
                deque.offer(0)
            }
            answer += 1
        }
        return answer
    }
}