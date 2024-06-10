from PIL import Image, ImageSequence
import math
import textwrap

class ImageConverter():
    def __init__(self, path): ##Image initialization (accepts the path to the image)
        self.Image_file = Image.open(path).convert('RGBA')
        self.path = path
    
    def _ReSize(self, new_size): ## Mandatory resize with the original class does not work
        self.resImage_file = self.Image_file.resize(new_size)
        
    def _Comparison(self, color_1, color_2): ## Returns the difference between two colors
        return ((color_1[0]-color_2[0])**2+(color_1[1]-color_2[1])**2+(color_1[2]-color_2[2])**2)**0.5
    
    def ToPNG(self): ## Makes a temporary fix to avoid detecting GIFs by appending an extra character to the file path
        self.path += 'u'
    
    def _GIFunpack(self, size): ## Temporary fix to convert a GIF into a single image where frames are stacked vertically
        im = self.Image_file
        frames = ImageSequence.Iterator(im)
        images = []
        for i in frames:
            images.append(i.resize(size))
        widths, heights = zip(*(i.size for i in images))
        total_width = max(widths)
        max_height = sum(heights)
        new_im = Image.new('RGBA', (total_width, max_height))
        x_offset = 0
        for im in images:
            new_im.paste(im, (0, x_offset))
            x_offset += im.size[1]
        self.resImage_file = new_im
    
    def _Average(self, mass): ## Calculates the average color between colors in the given array
        color_sum = [0, 0, 0]
        for i in mass:
            color_sum = [color_sum[0]+i[0], color_sum[1]+i[1], color_sum[2]+i[2]]
        len_list = len(mass)
        color_sum = [color_sum[0]/len_list, color_sum[1]/len_list, color_sum[2]/len_list]
        return color_sum
    
    def _СreatImageMap(self): ## Converts images into a two-dimensional matrix of colors
        self.Image_Map = self.resImage_file.load()
    
    def _СreatImageCode(self, size, sensitivity, load): ## Converts the image into a set of monochrome lines and writes them in a format understandable by the receiving part
        char = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" ## Alphabet used to convert numbers into base-36
        load.set_progress(0)
        lines = size[1]
        columns = size[0]
        self.Image_Code = ""
        buf = ""
        for line in range(lines):
            column = 0
            load.set_progress(((line/lines)*100))
            while column < columns:
                This_Line_len = 1
                color = self.Image_Map[column, line]
                column += 1
                color_list = [color]
                if color[3] >= 150:
                    while column < columns and This_Line_len < 35 and self._Comparison(self.Image_Map[column, line], color) < (sensitivity)*10:
                        color_list.append(self.Image_Map[column, line])
                        column += 1
                        This_Line_len += 1
                    colorx = self._Average(color_list)
                    if abs(colorx[0]-colorx[1]) >= 5 or abs(colorx[1]-colorx[2]) >= 5 or abs(colorx[0]-colorx[2]) >= 5:
                        buf += char[This_Line_len] + char[math.floor(colorx[0]/8)] + char[math.floor(colorx[1]/8)] + char[math.floor(colorx[2]/8)]
                    else:
                        buf += char[This_Line_len] + "-" + char[math.floor(colorx[2]/8)]
                else:
                    while column < columns and This_Line_len < 35 and (self.Image_Map[column,line][3] < 150):
                        column += 1
                        This_Line_len += 1
                    buf += char[This_Line_len] + "_"
            self.Image_Code += buf
            buf = "" 
    
    def convert(self, Size, sensitivity, flag, load): ## Method called to create the image code
        if self.path[-4:] == ".gif":
            self._GIFunpack(Size)
            width, height = self.resImage_file.size
            Size = [width, height]
        else:
            self.Image_file = self.Image_file.convert('RGBA')
            self._ReSize(Size)
        self._СreatImageMap()
        self._СreatImageCode(Size, sensitivity, load)
        if flag: ## Adds a header to the code if the flag is set
            self.Image_Code = str(Size[0])+"x"+str(Size[1])+"."+ self.Image_Code
        return self.Image_Code
