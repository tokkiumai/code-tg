function solve(nums, k) {
  if (!nums || !k) {
    return false
  }
  while (nums.length) {
    let num = nums.pop()
    if (nums.includes(k - num)) {
      return true
    }
  }
  return false
}

module.exports = solve
