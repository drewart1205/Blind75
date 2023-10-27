def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        seen = []
        max_area = area = 0
        l = len(height)
        i = 0
        j = l
        w = j-i
        h = min(height[i], height[j])
        area = h * w
        for w in range(l, 0, -1)
        
        for i in range(l):
            if height[i] == 0:
                continue
            for j in range(l, i, -1):
                w = j - i
                
                area = w * h
                if area > max_area:
                    max_area = area
        return max_area