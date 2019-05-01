import glob
markdown = ''

with open('cycle.txt') as afile:
    data = afile.read().split('	')

cycle = []

for i in data:
    try:
        float(i)
        cycle.append(i)
    except ValueError:
        pass
    
gifs = glob.glob('*.gif')


for i in range(len(gifs)):
    markdown += '![Cycle:{}][{}]'.format(cycle[i],gifs[i]) + '\n'


print(markdown)
    
    
