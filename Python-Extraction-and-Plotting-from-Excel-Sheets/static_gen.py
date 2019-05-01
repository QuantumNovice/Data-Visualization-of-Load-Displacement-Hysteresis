import glob
html = '''
<html>

'''
figure = '''
<figure>
	<table>
	<tr>
		<th>
		<img src="{}" alt="Trulli" style="width:90%">
		<figcaption>Cycle {}</figcaption>
		</th>
		
		<th>
		<img src="{}" alt="Trulli" style="width:90%">
		<figcaption>Cycle {}</figcaption>
		</th>
	</tr>
	
	</table>
</figure>
'''

end = '</html>'

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


for i in range(len(gifs)-1):
    html += figure.format(gifs[i], cycle[i],gifs[i+1], cycle[i+1])

html += end

with open('index.html', 'w') as afile:
    afile.write(html)
    
    
