class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        max_len = 0
        depth_len = {0: 0}  # depth -> total length up to that depth

        for line in input.split('\n'):
            # depth = number of leading tabs
            depth = line.count('\t')
            
            # name without tabs
            name = line.lstrip('\t')
            
            # if it's a file
            if '.' in name:
                # total path = parent length + filename length
                max_len = max(max_len, depth_len[depth] + len(name))
            else:
                # it's a directory
                # store: parent length + directory name + '/' 
                depth_len[depth + 1] = depth_len[depth] + len(name) + 1

        return max_len

        