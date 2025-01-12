impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut nums_with_indices: Vec<(i32, usize)> = nums.iter().cloned().zip(0..).collect();
        nums_with_indices.sort_unstable();

        let (mut left, mut right) = (0, nums_with_indices.len() - 1);
        while left < right {
            let sum = nums_with_indices[left].0 + nums_with_indices[right].0;
            if sum == target {
                return vec![nums_with_indices[left].1 as i32, nums_with_indices[right].1 as i32];
            } else if sum < target {
                left += 1;
            } else {
                right -= 1;
            }
        }
        vec![]
    }
}