#!/usr/bin/python
import pygame,sys
from pygame.locals import *
import os.path
import random
pygame.init()
size=[1000,600]
clock = pygame.time.Clock()
white=(255,255,255)
black=(0,0,0)
headfont=pygame.font.Font(None,30)
writefont=pygame.font.Font(None,25)
screen = pygame.display.set_mode(size)
screen.fill(white)
cord_wx=17
cord_x=30
cord_wy=80
cord_y=100
cord_x_pen=65
cord_y_pen=105
count=0
draw_line=1
write_line=1
write_count=0
overhead_time=0
process_list=[]
color_list=['0xBF62D9','0x40C2D8','0xDB92A9','0xCFDA68','0x9BE804','0x0461A4','0xBC3C0E']
color_dict={}
s = pygame.display.get_surface()
def draw(line,switch_time,schedule):
	global cord_x
	global cord_y
	global draw_line
	global color_dict
	global s
	flag=1
	
	if switch_time==0:
		
		p=pygame.draw.rect(screen,black,[cord_x,cord_y,95,30],2)
		s.fill(Color(color_dict[str((line.split(':'))[1])]), p)
		p=pygame.draw.rect(screen,black,[cord_x,cord_y,95,30],3)
	else:
		if schedule:
			p=pygame.draw.rect(screen,black,[cord_x,cord_y,40,30],2)
			s.fill(Color("black"),p)
			p=pygame.draw.rect(screen,black,[cord_x,cord_y,40,30],2)
			flag=0
		else:
			p=pygame.draw.rect(screen,black,[cord_x,cord_y,95,30],2)
			s.fill(Color(color_dict[str((line.split(':'))[1])]), p)
			p=pygame.draw.rect(screen,black,[cord_x,cord_y,95,30],2)
	if (cord_x+75)>900 and draw_line==1:
		cord_x=30
		cord_y=200
		draw_line=draw_line+1
	elif (cord_x+75)>900 and draw_line==2:
		cord_x=30
		cord_y=300
		draw_line=draw_line+1
	elif (cord_x+75)>900 and draw_line==3:
		cord_x=30
		cord_y=400
	elif flag:
		cord_x+=95
	else:
		cord_x+=40
def write(line,switch_time, schedule):
	global cord_wx
	global cord_wy
	global write_count
	global write_line
	global cord_x_pen
	global cord_y_pen
	flag=1
	add=0
	if switch_time==0:
		
		writetext=writefont.render(str((line.split(':'))[0]),2,[0,0,0])
		screen.blit(writetext,[cord_wx,cord_wy])
		writetext=writefont.render(str((line.split(':'))[1]),2,[0,0,0])
		screen.blit(writetext,[cord_x_pen,cord_y_pen])
		write_count+=1	
		
	else:
		if schedule:
			writetext=writefont.render(str((line.split(':'))[0]),2,[0,0,0])
			screen.blit(writetext,[cord_wx,cord_wy])
			writetext=writefont.render('$',2,[255,255,255])
			screen.blit(writetext,[cord_x_pen,cord_y_pen])
			write_count+=1
			flag=0
			
		else:
			writetext=writefont.render(str((line.split(':'))[0]),2,[0,0,0])
			screen.blit(writetext,[cord_wx,cord_wy])
			writetext=writefont.render(str((line.split(':'))[1]),2,[0,0,0])
			screen.blit(writetext,[cord_x_pen,cord_y_pen])
			write_count+=1
			
	if (cord_wx+95)>900 and write_line==1:
		if switch_time!=0:
			if schedule:
				cord_x_pen=65
			else:
				cord_x_pen=45
		else:
			cord_x_pen=65
		cord_y_pen=205
		cord_wx=15
		cord_wy=180
		write_line=write_line+1
	elif (cord_wx+95)>900 and write_line==2:
		if switch_time!=0:
			if schedule:
				cord_x_pen=65
			else:
				cord_x_pen=45
		else:
			cord_x_pen=65
		cord_wx=15
		cord_wy=280
		cord_y_pen=305
		write_line=write_line+1
	elif (cord_wx+95)>900 and write_line==3:
		if switch_time!=0:
			if schedule:
				cord_x_pen=65
			else:
				cord_x_pen=45
		else:
			cord_x_pen=65
		cord_wx=15
		cord_wy=380
		cord_y_pen=405
	elif flag:
		cord_wx+=95+add
		if switch_time!=0:
			if schedule:
				cord_x_pen+=95
			else:
				cord_x_pen+=70
		else:
			cord_x_pen+=95
	else:
		cord_wx+=40
		cord_x_pen+=65
	if count==write_count:
				c=int((line.split(':'))[0])+int((line.split(':'))[2])
				writetext=writefont.render(str(c),2,[0,0,0])
				screen.blit(writetext,[cord_wx,cord_wy])	
				return
	add+=10		
	
def blit_times(line):
	if 'TRnd' in line:
		c= line.split(':')[1]
		writetext=writefont.render("AVERAGE TURN AROUND TIME="+str(c.strip('\n')),2,[0,0,0])
		screen.blit(writetext,[50,(cord_y+100)])
	elif 'Wait' in line:
		writetext=writefont.render("AVERAGE WAIT TIME="+(line.split(':')[1]).strip('\n'),2,[0,0,0])
		screen.blit(writetext,[50,(cord_y+150)])
def gantt(caption,f):
	global count
	global overhead_time
	global process_list
	global color_list
	global color_dict
	caption=caption.split('.')[0]
	caption=caption.swapcase()
	caption=caption.replace('_',' ')
	pygame.display.set_caption(caption)
	Page_lines=f.readlines()
	if 'scheduler'in Page_lines[2]:
		overhead=True
		if overhead:
			overhead_time=((Page_lines[2]).split(':'))[2]
	for line in Page_lines:
			if ':' in line and not('time' in line):
				count+=1
				if not((line.split(':'))[1] in process_list): 
						process_list.append((line.split(':'))[1])
				for i in range(len(process_list)):
					color_dict.update({process_list[i]:color_list[i]})
	for line in Page_lines:
			if ':' in line and not('time' in line):
				if 'scheduler' in line:
					draw(line,overhead_time,True)
					write(line,overhead_time,True)
				else:
					
					draw(line,overhead_time,False)
					write(line,overhead_time,False)
				
			if 'time' in line:
				blit_times(line)
	name=(caption.split('.'))[0]
	name=name.replace('_',' ')	
	headtext=headfont.render(str((name.split('.'))[0]),1,[0,0,0])
	screen.blit(headtext,[40,20])
	while True:
		seconds = clock.tick()/1000.0
		for event in pygame.event.get():
        		if event.type == pygame.QUIT:
        			pygame.quit()
            			sys.exit()
            			break
            	pygame.display.update()	
if __name__=="__main__" :
	if len(sys.argv) >2:
		raise Exception("Too Many Arguments Passed")
	else:
		if os.path.isfile(str(sys.argv[1])):
			f=open(sys.argv[1])
			gantt(sys.argv[1],f)
		else:
			raise Exception("FileNotFoud!!")	
