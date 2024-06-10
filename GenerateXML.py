import textwrap

def Creat_obj(text, number, name): # Create a property text object
    objs = """<c type="58">
                <object id=\""""+str(number+4)+"""" n=\"""" +name+str(number)+"""" v=\""""+text+"""">
                    <pos x="0.5" y="-2.5"/>
                </object>
            </c>"""
    return objs
    
def CompileImage(code, name, IMGsize): # Write to the controller created to display images
    texts = textwrap.wrap(text = code, width = 4096)
    objs = ""
    number = 1
    for text in texts:
        objs += Creat_obj(text, number, name)
        number += 1      
    return """<?xml version="1.0" encoding="UTF-8"?>
<microprocessor name=\""""+name+"""" description=\""""+"screen size: "+str(IMGsize[0]//32)+"X"+str(IMGsize[1]//32)+"""" hide_in_inventory="false" width="1" length="1" id_counter="5" id_counter_node="1" transform_index="0" sym0="0" sym1="0" sym2="0" sym3="0" sym4="0" sym5="0" sym6="0" sym7="0" sym8="0" sym9="0" sym10="0" sym11="0" sym12="0" sym13="0" sym14="0" sym15="0">
    <nodes>
        <n id="1" component_id="4" built_slot_index="0">
            <node orientation="0" label="OUT" mode="0" type="6" description="" flags="0">
                <position x="0" y="0" z="0"/>
            </node>
        </n>
    </nodes>
    <group id="0">
        <pos x="0" y="0"/>
        <data type="0" name="" desc="">
            <inputs/>
            <outputs/>
        </data>
        <components>
            <c type="56">
                <object id="1" script='IMG=""
w = """+str(IMGsize[0])+"""
Coun = 200
f = true
a = 1
while f do
    get = property.getText(&apos;"""+name+"""&apos;..a)
    a=a+1
    IMG=IMG..get
    if get == "" then f = false end
end
mass = {}
    a = 1
    l = 1
function onTick()
    t = 1
    while IMG ~= "" and t &lt; Coun do
        if IMG:sub(2,2) ~= "_" and IMG:sub(2,2) ~= "-" then
            mass[#mass+1] = {pos = {a-1, l-1, a+tonumber(IMG:sub(1,1),36)-1,l-1}, 
            col = {tonumber(IMG:sub(2,2),36)*2.5,tonumber(IMG:sub(3,3),36)*2.5, tonumber(IMG:sub(4,4),36)*2.5}}
            a = a+tonumber(IMG:sub(1,1),36)
            if a &gt; w then a = 1 l = l+1 end
            IMG = IMG:sub(5,-1)
            t=t+1
        elseif IMG:sub(2,2) ~= "_" then
            mass[#mass+1] = {pos = {a-1, l-1, a+tonumber(IMG:sub(1,1),36)-1,l-1}, 
            col = {tonumber(IMG:sub(3,3),36)*2.5,tonumber(IMG:sub(3,3),36)*2.5, tonumber(IMG:sub(3,3),36)*2.5}}
            a = a+tonumber(IMG:sub(1,1),36)
            if a &gt; w then a = 1 l = l+1 end
            IMG = IMG:sub(4,-1)
            t=t+1
        else
            t=t+1
            a = a+tonumber(IMG:sub(1,1),36)
            if a &gt; w then a = 1 l = l+1 end
            IMG = IMG:sub(3,-1)
        end
    end
end



function onDraw()
    for i, line in ipairs(mass) do
        screen.setColor(table.unpack(line.col))
        screen.drawLine(table.unpack(line.pos))
    end
end
'>
                    <pos x="0.5" y="-1.5"/>
                    <in1 component_id="0" node_index="0">
                        <v bools="0" 01="0" 02="0" 03="0" 04="0" 05="0" 06="0" 07="0" 08="0" 09="0" 10="0" 11="0" 12="0" 13="0" 14="0" 15="0" 16="0" 17="0" 18="0" 19="0" 20="0" 21="0" 22="0" 23="0" 24="0" 25="0" 26="0" 27="0" 28="0" 29="0" 30="0" 31="0" 32="0"/>
                    </in1>
                    <in2 component_id="0" node_index="0">
                        <v/>
                    </in2>
                    <out1>
                        <v bools="0" 01="0" 02="0" 03="0" 04="0" 05="0" 06="0" 07="0" 08="0" 09="0" 10="0" 11="0" 12="0" 13="0" 14="0" 15="0" 16="0" 17="0" 18="0" 19="0" 20="0" 21="0" 22="0" 23="0" 24="0" 25="0" 26="0" 27="0" 28="0" 29="0" 30="0" 31="0" 32="0"/>
                    </out1>
                    <out2>
                        <v/>
                    </out2>
                </object>
            </c>
            """+objs+"""</components>
        <components_bridge>
            <c type="7">
                <object id="4">
                    <pos x="2" y="-1.5"/>
                    <in1 component_id="1" node_index="1">
                        <v/>
                    </in1>
                    <out1>
                        <v/>
                    </out1>
                </object>
            </c>
        </components_bridge>
        <groups/>
        <component_states>
        </component_states>
        <component_bridge_states>
        </component_bridge_states>
        <group_states/>
    </group>
</microprocessor>"""

def CompileGIF(code, name, IMGsize):  # Write to the controller created to display GIFs
    texts = textwrap.wrap(text = code, width = 4096)
    objs = ""
    number = 1
    for text in texts:
        objs += Creat_obj(text, number, name)
        number += 1      
    return """<?xml version="1.0" encoding="UTF-8"?>
    <microprocessor name=\""""+name+"""" description=\""""+"screen size: "+str(IMGsize[0]//32)+"X"+str(IMGsize[1]//32)+"""" hide_in_inventory="false" width="1" length="1" id_counter="5" id_counter_node="1" transform_index="0" sym0="0" sym1="0" sym2="0" sym3="0" sym4="0" sym5="0" sym6="0" sym7="0" sym8="0" sym9="0" sym10="0" sym11="0" sym12="0" sym13="0" sym14="0" sym15="0">
        <nodes>
            <n id="1" component_id="4" built_slot_index="0">
                <node orientation="0" label="OUT" mode="0" type="6" description="" flags="0">
                    <position x="0" y="0" z="0"/>
                </node>
            </n>
        </nodes>
        <group id="0">
            <pos x="0" y="0"/>
            <data type="0" name="" desc="">
                <inputs/>
                <outputs/>
            </data>
            <components>
                <c type="56">
                    <object id="1" script='name = \""""+name+""""
    speed = """+str(IMGsize[1])+"""
    function copy(m)
    local mass = {}
        for i, v in ipairs(m) do
            mass[i]=v
        end
        return mass
    end


    function drawimage(y,mass)
        for i, line in ipairs(mass) do
            screen.setColor(table.unpack(line.col))
            screen.drawLine(line.pos[1], y, line.pos[3], y)
        end
    end
    t = 0
    im = ""
    count=0
    for i = 1, 70 do
     count=count+1
     im = im.. property.getText(name.. count)
    end
    r = 1
        while im:sub(r,r) ~= "x" do
            r = r + 1
        end
        w = tonumber(im:sub(1,r-1))
        im = im:sub(r+1,-1)
        r = 1
        while im:sub(r,r) ~= "." do
            r = r + 1
        end
        h = tonumber(im:sub(1,r-1))
        im = im:sub(r+1,-1)
    mass = {}
    mmm={}
    x = 0
    t = 0
    a = 1
    l = 1
    tt=0
    buf = ""

    function onTick()
        tt=(tt+1)%6
        if count &lt; 2000 then
        for i = 1, 70 do
            count=count+1
            im = im.. property.getText(name.. count)
        end	
        end
        while (buf ~= "" or im ~= "") and l - t + 1 &lt; 20 do
            if #buf &lt; 6 and im ~= "" then
                buf = buf.. im:sub(1, 200)
                im = im:sub(201, -1)
            end
            if buf:sub(2,2) ~= "_" and buf:sub(2,2) ~= "-" then
                mass[#mass+1] = {pos = {(a-1), 0, (a+tonumber(buf:sub(1,1),36)-1),0}, 
                col = {tonumber(buf:sub(2,2),36)*2.5,tonumber(buf:sub(3,3),36)*2.5, tonumber(buf:sub(4,4),36)*2.5}}
                a = a+tonumber(buf:sub(1,1),36)
                if a &gt; w then 
                    mmm[l] = copy(mass)
                    mass = {}
                    a = 1 
                    l = l+1 
                end
                buf = buf:sub(5,-1)
            elseif buf:sub(2,2) ~= "_" then
                mass[#mass+1] = {pos = {(a-1), 0, (a+tonumber(buf:sub(1,1),36)-1),0}, 
                col = {tonumber(buf:sub(3,3),36)*2.5,tonumber(buf:sub(3,3),36)*2.5, tonumber(buf:sub(3,3),36)*2.5}}
                a = a+tonumber(buf:sub(1,1),36)
                if a &gt; w then 
                    mmm[l] = copy(mass)
                    mass = {}
                    a = 1 
                    l = l+1 
                end
                buf = buf:sub(4,-1)
            else
                a = a+tonumber(buf:sub(1,1),36)
                if a &gt; w then
                    mmm[l] = copy(mass)
                    mass = {}
                    a = 1 
                    l = l+1 	
                end
                buf = buf:sub(3,-1)
            end
        end
        t = l+0
        if #mmm &gt;= h-1 and tt == 0 then
        x = (x + speed)
        if x &gt;= #mmm-5 then x = 0 end
        end
    end

    function onDraw()
    if #mmm &gt;= h-1 then
        for i = 0, speed do
            drawimage((i),mmm[math.floor((x+i)%#mmm)+1])
        end
    else
        screen.setColor(20, 0, 0)
        screen.drawText(20, 0, "LOADING:\\n"..math.floor(#mmm/h*100).. "%")
    end
    end
    '>
                        <pos x="0.5" y="-1.5"/>
                        <in1 component_id="0" node_index="0">
                            <v bools="0" 01="0" 02="0" 03="0" 04="0" 05="0" 06="0" 07="0" 08="0" 09="0" 10="0" 11="0" 12="0" 13="0" 14="0" 15="0" 16="0" 17="0" 18="0" 19="0" 20="0" 21="0" 22="0" 23="0" 24="0" 25="0" 26="0" 27="0" 28="0" 29="0" 30="0" 31="0" 32="0"/>
                        </in1>
                        <in2 component_id="0" node_index="0">
                            <v/>
                        </in2>
                        <out1>
                            <v bools="0" 01="0" 02="0" 03="0" 04="0" 05="0" 06="0" 07="0" 08="0" 09="0" 10="0" 11="0" 12="0" 13="0" 14="0" 15="0" 16="0" 17="0" 18="0" 19="0" 20="0" 21="0" 22="0" 23="0" 24="0" 25="0" 26="0" 27="0" 28="0" 29="0" 30="0" 31="0" 32="0"/>
                        </out1>
                        <out2>
                            <v/>
                        </out2>
                    </object>
                </c>
                """+objs+"""</components>
            <components_bridge>
                <c type="7">
                    <object id="4">
                        <pos x="2" y="-1.5"/>
                        <in1 component_id="1" node_index="1">
                            <v/>
                        </in1>
                        <out1>
                            <v/>
                        </out1>
                    </object>
                </c>
            </components_bridge>
            <groups/>
            <component_states>
            </component_states>
            <component_bridge_states>
            </component_bridge_states>
            <group_states/>
        </group>
    </microprocessor>"""

def CompileSprite(code, name):  # Write to the controller without a script (just a sprite that can be used at your discretion)
    texts = textwrap.wrap(text = code, width = 4096)
    objs = ""
    number = 1
    for text in texts:
        objs += Creat_obj(text, number, name)
        number += 1      
    return """<?xml version="1.0" encoding="UTF-8"?>
<microprocessor name=\""""+name+"""" description=\""""+"""" hide_in_inventory="false" width="1" length="1" id_counter="5" id_counter_node="1" transform_index="0" sym0="0" sym1="0" sym2="0" sym3="0" sym4="0" sym5="0" sym6="0" sym7="0" sym8="0" sym9="0" sym10="0" sym11="0" sym12="0" sym13="0" sym14="0" sym15="0">
    <nodes>
        <n id="1" component_id="4" built_slot_index="0">
            <node orientation="0" label="OUT" mode="0" type="6" description="" flags="0">
                <position x="0" y="0" z="0"/>
            </node>
        </n>
    </nodes>
    <group id="0">
        <pos x="0" y="0"/>
        <data type="0" name="" desc="">
            <inputs/>
            <outputs/>
        </data>
        <components>
            """+objs+"""</components>
        <components_bridge>
            
        </components_bridge>
        <groups/>
        <component_states>
        </component_states>
        <component_bridge_states>
        </component_bridge_states>
        <group_states/>
    </group>
</microprocessor>"""