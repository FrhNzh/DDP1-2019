def decipher(teks, kotoran):
	''' fungsi untuk membersihkan teks dari kotoran '''
	
	if len(teks) == 1:
		if teks not in kotoran:
			return teks
		else:
			return ''
	elif teks[0] in kotoran:
		return decipher(teks[1::], kotoran)
	else:
		return teks[0] + decipher(teks[1::], kotoran)