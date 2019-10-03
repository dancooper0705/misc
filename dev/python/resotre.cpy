from PIL import Image, ImageFilter

def copy(dst_img, dst_pos, src_img, src_pos, rect):
    #print("dst_pos: " + str(dst_pos) + ", src_pos: " + str(src_pos))
    for i in range(rect[0]):
        for j in range(rect[1]):
            pixel = src_img.getpixel((src_pos[0]+i,src_pos[1]+j))
            dst_img.putpixel((dst_pos[0]+i,dst_pos[1]+j), pixel)
            #print("i: " + str(i) + ", j: " + str(j))

def main():
    perm = [32 ,21 ,22 ,16 ,14 ,60 ,29 ,39 ,33 ,31 ,54 ,26 ,10 ,20 ,1 ,41 ,56 ,28 ,12 ,17 ,25 ,58 ,59 ,43 ,45 ,46 ,44 ,18 ,0 ,3 ,62 ,6 ,38 ,48 ,13 ,63 ,27 ,19 ,50 ,51 ,23 ,37 ,40 ,53 ,42 ,24 ,61 ,57 ,52 ,15 ,5 ,34 ,36 ,4 ,35 ,8 ,49 ,9 ,2 ,55 ,7 ,11 ,47 ,30]
    shuffled_img = Image.open('a.png')
    source_img = Image.open("b.png")
    print("shuffled_img: " + str(shuffled_img))
    new_img = Image.new("RGB", (512, 512))
    if new_img == source_img:
        print("new_img == source_img")
    else:
        print("new_img != source_img")
    #copy(new_img, (0,0), img, (0, 256), (64,64))
    for i in range(64):
        ix = i % 8
        iy = i // 8
        j = perm[i]
        jx = j % 8
        jy = j // 8
        #print("i: " + str(i) + ", ix: " + str(ix) + ", iy: " + str(iy))
        #print("j: " + str(j) + ", jx: " + str(jx) + ", jy: " + str(jy))
        #print("i: " + str(i) + ", j: " + str(j))
        copy(new_img, (ix*64,iy*64), shuffled_img, (jx*64,jy*64), (64,64))
    if new_img == source_img:
        print("new_img == source_img")
    else:
        print("new_img != source_img")
    #source_img.show()
    new_img.show()
    same = 1
    new_img.save("c.png")
    for i in range(512):
        for j in range(512):
            if new_img.getpixel((i,j)) != source_img.getpixel((i,j)):
                print("i: " + str(i) + ", j: " + str(j) + " not the same" + new_img.getpixel((i,j)) + ", " + source_img.getpixel((i,j)))
                same = 0
    print("same: " + str(same))
if __name__ == "__main__":
    main()

