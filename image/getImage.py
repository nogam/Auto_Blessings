from GlobalVars import IMAGE_INPUT_DIR



def getimage(ts):
    path = IMAGE_INPUT_DIR + 'input_' + str(ts) + '.jpg'
    return path