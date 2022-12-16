class Solution {
    fun solution(n: Int): IntArray {
        var answer = intArrayOf()
        var triangle = Array<IntArray>(n) {i -> IntArray(i + 1){j -> 0} }
        var num = 0
        var y = 0
        var x = 0
        for(i in 0 until (n / 3) + (if (n % 3 == 0) 0 else 1)){
            if(y == n - i - 1) triangle[y][x] = num + 1
            while(y < n - i - 1){
                num += 1
                triangle[y][x] = num
                y += 1
            }
            while(x < n - i - (i + 1)){
                num += 1
                triangle[y][x] = num
                x += 1
            }
            while(2*i < y){
                num += 1
                triangle[y][x] = num
                y -= 1
                x -= 1
            }
            y += 2
            x += 1
        }
        triangle.forEach { arr -> answer += arr }
        return answer
    }
}