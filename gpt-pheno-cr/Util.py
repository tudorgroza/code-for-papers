def parseGPTResults(content):
    hpoData = {}
    procContent = content.replace('https://hpo.jax.org/app/browse/term/HP:0', '')
    segs = procContent.split('HP:0')
    for i in range(1, len(segs)):
        temp = 'HP:0' + segs[i]
        target = temp[:10]

        count = 0
        if target in hpoData:
            count = hpoData[target]
        count += 1
        hpoData[target] = count
    return hpoData
