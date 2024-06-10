tn=tonumber
function Convert(IMG)
local mass={}
local a=1
local l=1
local r=1
while IMG:sub(r,r)~="x"do
r=r+1
end
local w=tn(IMG:sub(1,r-1))
IMG=IMG:sub(r+1,-1)
r=1
while IMG:sub(r,r)~="."do
r=r+1
end
local h=tn(IMG:sub(1,r-1))
IMG=IMG:sub(r+1,-1)
while IMG~=""do
if IMG:sub(2,2)~="_"and IMG:sub(2,2)~="-"then
mass[#mass+1]={pos={a-1,l-1,a+tn(IMG:sub(1,1),36)-1,l-1}, 
col = {tn(IMG:sub(2,2),36)*2.5,tn(IMG:sub(3,3),36)*2.5,tn(IMG:sub(4,4),36)*2.5}}
a = a+tn(IMG:sub(1,1),36)
if a>w then a=1 l=l+1 end
IMG=IMG:sub(5,-1)
elseif IMG:sub(2,2)~="_"then
mass[#mass+1]={pos={a-1,l-1,a+tn(IMG:sub(1,1),36)-1,l-1}, 
col={tn(IMG:sub(3,3),36)*2.5,tn(IMG:sub(3,3),36)*2.5,tn(IMG:sub(3,3),36)*2.5}}
a=a+tn(IMG:sub(1,1),36)
if a>w then a=1 l=l+1 end
IMG=IMG:sub(4,-1)
else
a=a+tn(IMG:sub(1,1),36)
if a>w then a=1 l=l+1 end
IMG=IMG:sub(3,-1)
end
end
return mass
end
function drawimage(x,y,mass)
for i, line in ipairs(mass) do
screen.setColor(table.unpack(line.col))
screen.drawLine(line.pos[1]+x, line.pos[2]+y, line.pos[3]+x, line.pos[4]+y)
end
end