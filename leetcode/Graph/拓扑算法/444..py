class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """

        child = {}
        par = {}

        for num in org:
            child[num] = set()
            par[num] = set()

        for node in seqs:
            if not node:
                continue
            for i in range(len(node)):
                # 从i节点往后的都是child
                for val in node[i + 1:]:
                    child[node[i]].add(val)

                # 从i节点往前的都是parent
                for val in node[:i]:
                    par[node[i]].add(val)


        print("par", par)
        print("child", child)

        queue = []
        res = []

        no_par_node = [ch for ch in par if len(par[ch]) == 0]
        for ch in no_par_node:
            queue.append(ch)
            del par[ch]

        if len(queue) > 1 or not queue:
            return False

        while queue:
            if len(queue) > 1:
                return False

            cur_node = queue.pop()
            res.append(cur_node)
            # 先消除子节点 与父节点的连接, 再把无父连接 的子节点放进queue里
            for ch in child[cur_node]:

                par[ch].remove(cur_node)
                if len(par[ch]) == 0:
                    queue.append(ch)
                    del par[ch]

        print(res)
        return org == res