import java.util.*

class Solution {
    fun solution(k: Int, tangerine: IntArray): Int {
        var answer: Int = 0
        val map = mutableMapOf<Int, Int>()
        for (t in tangerine){
            val size = map.get(t)
            if(size == null){
                map.put(t, 1)
                continue
            }
            map.set(t, size + 1)
        }
        var sizeAndNumber = ArrayList<IntArray>()
        var values = map.values.sortedDescending()
        var total = 0
        for(value in values){
            total += value
            answer += 1
            if(total >= k) break
        }
        return answer
    }
}