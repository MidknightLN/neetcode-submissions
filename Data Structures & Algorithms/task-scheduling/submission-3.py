class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # N 代表中間要間隔幾格  所以在計算上 實際上每一組是 n+1
        # 然後最後一組再算  有多少相同的最大值
        from collections import Counter

        counts = Counter(tasks)
        max_freq = max(counts.values())
        count_max_freq = sum(1 for freq in counts.values() if freq == max_freq)
        ans = (max_freq-1) * (n+1) + count_max_freq
        return max(len(tasks), ans)

        