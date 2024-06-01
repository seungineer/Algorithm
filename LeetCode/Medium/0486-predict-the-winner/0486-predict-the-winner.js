/**
 * @param {number[]} nums
 * @return {boolean}
 */
var predictTheWinner = function(nums) {
    let total_nums = 0;
    for (let i = 0; i<nums.length; i++){
        total_nums += nums[i];
    }

    let dict = {};
    function dfs(l, r, isPlayer1){ // l, r 중 선택할 때 (P1-P2가 최대가 되도록) num을 선택
        if ([l, r, isPlayer1] in dict){
            return dict[[l, r, isPlayer1]];
        }
        if (l > r){
            return 0;
        }
        
        let num = 0;
        if (isPlayer1){
            num = Math.max(dfs(l+1, r, false) + nums[l], dfs(l, r-1, false) + nums[r]);
        }
        else{
            num = Math.min(dfs(l+1, r, true), dfs(l, r-1, true));
        }
        dict[[l, r, isPlayer1]] = num;
        return num;
    }
    return dfs(0, nums.length -1, true) >= total_nums/2;
};