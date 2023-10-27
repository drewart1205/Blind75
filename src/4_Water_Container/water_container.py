def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = 0
    l = len(height)
    seek_h = 0
    i = 0
    j = l - 1
    for w in range(l - 1, 0, -1):
        seek_h = int(max_area / w)
        
        h = min(height[i], height[j])
        if h > seek_h:
            max_area = h * w
        
        if height[i] > height[j]:
            j-=1
        else:
            i+=1
        
    return max_area