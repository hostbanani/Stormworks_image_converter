
--[[
This converter allows you to perform the same operation as the standard one using the string converter(property text): getAllLines(),
 and to modify other methods of image code usage.

For instance, by calling the getLine method on the converter object, you will get one line of the image each time, which is useful,
 for example, when displaying GIF animations.

Also, this principle forms the basis of a moving background. We draw the selected range of lines and can freely move the image and
 even loop it using the remainder of division to select the line number.

Furthermore, this method allows splitting the image processing into several ticks by converting only a certain number of lines at
 a time, and then adding them to the common array.
]]

-- Function to parse and convert a string into a structured format
function converter(text)
    -- Find the positions of 'x' and '.' in the input text
    local xPos, dotPos = text:find('x'), text:find('%.')
    
    -- Initialize the converter object
    return {
        size = {
            tonumber(text:sub(1, xPos - 1)), 
            tonumber(text:sub(xPos + 1, dotPos - 1))
        },
        code = text:sub(dotPos + 1, -1),
        currentLine = 1,
        buffer = "",
        
        -- Method to process a single line
        getLine = function(self)
            local lineData, column = {}, 0
            
            -- Process columns until the end of the line
            while column < self.size[1] do
                -- Ensure buffer has enough data
                if #self.buffer < 25 and #self.code > 0 then
                    self.buffer = self.buffer .. self.code:sub(1, 600)
                    self.code = self.code:sub(601, -1)
                end
                
                -- Process different cases based on the second character in the buffer
                local char1, char2, char3, char4 = self.buffer:sub(1, 1), self.buffer:sub(2, 2), self.buffer:sub(3, 3), self.buffer:sub(4, 4)
                if char2 == '-' then
                    local colorValue = tonumber(char3, 36) * 2.5
                    table.insert(lineData, {
                        pos = {column, self.currentLine, column + tonumber(char1, 36), self.currentLine},
                        col = {colorValue, colorValue, colorValue}
                    })
                    column = column + tonumber(char1, 36)
                    self.buffer = self.buffer:sub(4, -1)
                elseif char2 == '_' then
                    column = column + tonumber(char1, 36)
                    self.buffer = self.buffer:sub(3, -1)
                else
                    table.insert(lineData, {
                        pos = {column, self.currentLine, column + tonumber(char1, 36), self.currentLine},
                        col = {
                            tonumber(char2, 36) * 2.5, 
                            tonumber(char3, 36) * 2.5, 
                            tonumber(char4, 36) * 2.5
                        }
                    })
                    column = column + tonumber(char1, 36)
                    self.buffer = self.buffer:sub(5, -1)
                end
            end
            
            -- Increment line number for the next call
            self.currentLine = self.currentLine + 1
            return lineData
        end,
        
        -- Method to process all lines
        getAllLines = function(self)
            local allLines = {}
            
            -- Process each line until the end
            while self.currentLine <= self.size[2] do
                local lineData = self:getLine()
                table.move(lineData, 1, #lineData, #allLines + 1, allLines)
            end
            return allLines
        end
    }
end


--compression version

b=tonumber
l=table
function converter(d)
local i,j=d:find('x'
),d:find('%.'
)return{size={b(d:sub(1,i-1)),b(d:sub(i+1,j-1))},code=d:sub(j+1,-1),currentLine=1,buffer=""
,getLine=function(self)
local c,a={},0
while a<self.size[1]do
if#self.buffer<25 and#self.code>0 then
self.buffer=self.buffer..self.code:sub(1,600)self.code=self.code:sub(601,-1)
end
local e,f,k,m=self.buffer:sub(1,1),self.buffer:sub(2,2),self.buffer:sub(3,3),self.buffer:sub(4,4)
if f=='-'then
local g=b(k,36)*2.5
l.insert(c,{pos={a,self.currentLine,a+b(e,36),self.currentLine},col={g,g,g}})
a=a+b(e,36)self.buffer=self.buffer:sub(4,-1)
elseif f=='_'then
a=a+b(e,36)self.buffer=self.buffer:sub(3,-1)else l.insert(c,{pos={a,self.currentLine,a+b(e,36),self.currentLine},col={b(f,36)*2.5,b(k,36)*2.5,b(m,36)*2.5}})
a=a+b(e,36)self.buffer=self.buffer:sub(5,-1)
end
end
self.currentLine=self.currentLine+1
return c end,getAllLines=function(self)
local h={}
while self.currentLine<=self.size[2]do
local c=self:getLine()
l.move(c,1,#c,#h+1,h)
end
return h end}end