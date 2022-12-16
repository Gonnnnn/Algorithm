class Solution {
    fun solution(s: String): IntArray {
        val answer: IntArray = IntArray(s.length)
        val charMap = mutableMapOf<Char, Int>()
        for(c in s.withIndex()){
            var prevIdx: Int? = charMap.get(c.value)
            if(prevIdx == null) {
               prevIdx = c.index + 1
            }
            answer[c.index] = c.index - prevIdx
            charMap.put(c.value, c.index)
        }
        return answer
    }
}