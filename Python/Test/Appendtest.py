#some code here
a = 2
b = 1

print(a + b)

applyLine = 1#apply to wich line(line 1 = 0, line 2 = 1)
with open(__file__, 'r') as f:
  lines = f.read().split('\n')#make each line a str in a list called 'lines'
  val = int(lines[applyLine].split(' = ')[-1])#make an int to get whatever is after ' = ' to applyed line 
  new_line = 'a = {}'.format(val+1)#generate the new line
lines[applyLine] = new_line#update 'lines' to add the new line
write = "\n".join(lines)#create what to rewrite and store it in 'write' as str
with open(__file__, 'w') as f:
  f.write(write)#update the code