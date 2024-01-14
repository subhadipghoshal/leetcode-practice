use std::collections::HashMap;
use std::convert::TryInto;

struct Solution;

impl Solution {
    fn build_freq_dict(nums: Vec<i32>) -> HashMap<i32, i32> {
        let mut freq_dict = HashMap::new();

        for &num in nums.iter() {
            let counter = freq_dict.entry(num).or_insert(0);
            *counter += 1;
        }

        freq_dict
    }

    fn majority_element(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let freq_dict = Solution::build_freq_dict(nums);

        for (num, &freq) in freq_dict.iter() {
            if freq > (n / 2).try_into().unwrap() {
                return *num;
            }
        }

        panic!("No majority element found")
    }
}

fn main() {
    // Example usage
    let nums = vec![3, 3, 4, 2, 4, 4, 2, 4, 4];
    let result = Solution::majority_element(nums);
    println!("Majority Element: {}", result);
}
