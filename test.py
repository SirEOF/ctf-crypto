#!/usr/bin/env python3

def printArray(array):
	for line in array:
		print(line)

if __name__ == '__main__':
	import substitution as sub
	import analysis as ans
	from util import *
	from analysis import *

	# print(CipherInput(CipherType.reverse_alphabet, "uozdovhhob zigrxfozgrmt slmvbyzwtvi").decrypt()[0])

	# cipherArr = CipherInput(CipherType.cesar, "JedmRUT0sYMyReNlQOpdAYFqwPT0t2vqQPTgRPAyv2znAZvnueldRUTzvUTKsPRdueBztekyLYXat3BzvY9qsONrDaTPsYX0AYzzuqTrsYMyQeNdtaTcvOBaROIyQPE/", 1).decrypt()
	# print(cipherArr[0].generateCipherInput(CipherType.base64).decrypt()[0])

	# for cipher in cipherArr:
	# printArray(CipherInput(CipherType.base64, "RmluZCB0aGUgZmVtYWxlIGNyeXB0b2dyYXBoZXIgd2hvIHdvcmtlZCBhdCBSaXZlcmJhbmsgTGFib3JhdG9yaWVzLiBXaGF0IGhhcyBzaGUgYmVlbiBkdWJiZWQgYXM/").decrypt())
	# printArray(ans.sortByEnglishRank(sub.b64DecodeRotations(
	# 	'JedmRUT0sYMyReNlQOpdAYFqwPT0t2vqQPTgRPAyv2znAZvnueldRUTzvUTKsPRdueBztekyLYXat3BzvY9qsONrDaTPsYX0AYzzuqTrsYMyQeNdtaTcvOBaROIyQPE/', '.')))

	# print(sub.vigenereDecryptWithKey('mlal bw s mxwl', 'test'))
	# print(sub.findRepeatedSequenceOffsets('RIKVBIYBITHUSEVAZMMLTKASRNHPNPZICSWDSVMBIYFQEZUBZPBRGYNTBURMBECZQKBMBPAWIXSOFNUZECNRAZFPHIYBQEOCTTIOXKUNOHMRGCNDDXZWIRDVDRZYAYYICPUYDHCKXQIECIEWUICJNNACSAZZZGACZHMRGXFTILFNNTSDAFGYWLNICFISEAMRMORPGMJLUSTAAKBFLTIBYXGAVDVXPCTSVVRLJENOWWFINZOWEHOSRMQDGYSDOPVXXGPJNRVILZNAREDUYBTVLIDLMSXKYEYVAKAYBPVTDHMTMGITDZRTIOVWQIECEYBNEDPZWKUNDOZRBAHEGQBXURFGMUECNPAIIYURLRIPTFOYBISEOEDZINAISPBTZMNECRIJUFUCMMUUSANMMVICNRHQJMNHPNCEPUSQDMIVYTSZTRGXSPZUVWNORGQJMYNLILUKCPHDBYLNELPHVKYAYYBYXLERMMPBMHHCQKBMHDKMTDMSSJEVWOPNGCJMYRPYQELCDPOPVPBIEZALKZWTOPRYFARATPBHGLWWMXNHPHXVKBAANAVMNLPHMEMMSZHMTXHTFMQVLILOVVULNIWGVFUCGRZZKAUNADVYXUDDJVKAYUYOWLVBEOZFGTHHSPJNKAYICWITDARZPVU', 30))
	# print(sub.findPossibleKeyLengths('text bla ste text'))
	
	# print(sub.getStringsForKeyLength(4, 'PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU'))
	
	# print(sub.decryptVigionare('PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU'))
	

	# print(simpleEnglishFrequencyScore("""
	# 	Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf. Vz wsa twbhdg ubalmmzhdad qz hce vmhsgohuqbo ox kaakulmd gxiwvos, krgdurdny i rcmmstugvtawz ca tzm ocicwxfg jf "stscmilpy" oid "uwydptsbuci" wabt hce Lcdwig eiovdnw. Bgfdny qe kddwtk qjnkqpsmev ba pz tzm roohwz at xoexghzr kkusicw izr vrlqrwxist uboedtuuznum. Pimifo Icmlv Emf DI, Lcdwig owdyzd xwd hce Ywhsmnemzh Xovm mby Cqxtsm Supacg (GUKE) oo Bdmfqclwg Bomk, Tzuhvif'a ocyetzqofifo ositjm. Rcm a lqys ce oie vzav wr Vpt 8, lpq gzclqab mekxabnittq tjr Ymdavn fihog cjgbhvnstkgds. Zm psqikmp o iuejqf jf lmoviiicqg aoj jdsvkavs Uzreiz qdpzmdg, dnutgrdny bts helpar jf lpq pjmtm, mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk naf ohw Mzwbms umqcifm. Mtoej bts raj pq kjrcmp oo tzm Zooigvmz Khqauqvl Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa rcm a kbafzd-hzaumae kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf Zsrmsv'e Qjmhcfwig Dincmalwdm vt Eizqcekbqf Pnadqfnilg, ivzrw pq onsaafsy if bts yenmxckmwvf ca tzm Yoiczmehzr uwydptwze oid tmoohe avfsmekbqr dn eifvzmsbuqvl tqazjgq. Pq kmolm m dvpwz ab ohw ktshiuix pvsaa at hojxtcbefmewn, afl bfzdakfsy okkuzgalqzu xhwuuqvl jmmqoigve gpcz ie hce Tmxcpsgd-Lvvbgbubnkq zqoxtawz, kciup isme xqdgo otaqfqev qz hce 1960k. Bgfdny'a tchokmjivlabk fzsmtfsy if i ofdmavmz krgaqqptawz wi 1952, wzmz vjmgaqlpad iohn wwzq goidt uzgeyix wi tzm Gbdtwl Wwigvwy. Vz aukqdoev bdsvtemzh rilp rshadm tcmmgvqg (xhwuuqvl uiehmalqab) vs sv mzoejvmhdvw ba dmikwz. Hpravs rdev qz 1954, xpsl whsm tow iszkk jqtjrw pug 42id tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl lqhzreqzsy tzif vds vmmhc wsa eidcalq; vds ewfvzr svp gjmw wfvzrk jqzdenmp vds vmmhc wsa mqxivmzhvl. Gv 10 Esktwunsm 2009, fgtxcrifo mb Dnlmdbzt uiydviyv, Nfdtaat Dmiem Ywiikbqf Bojlab Wrgez avdw iz cafakuog pmjxwx ahwxcby gv nscadn at ohw Jdwoikp scqejvysit xwd "hce sxboglavs kvy zm ion tjmmhzd." Sa at Haq 2012 i bfdvsbq azmtmd'g widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo Tmzubb a kbmhptgzk dvrvwz wa efiohzd.
	# 	"""))

	# print(sub.vigenereDecryptWithKey("""Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf. Vz wsa twbhdg ubalmmzhdad qz hce vmhsgohuqbo ox kaakulmd gxiwvos, krgdurdny i rcmmstugvtawz ca tzm ocicwxfg jf "stscmilpy" oid "uwydptsbuci" wabt hce Lcdwig eiovdnw. Bgfdny qe kddwtk qjnkqpsmev ba pz tzm roohwz at xoexghzr kkusicw izr vrlqrwxist uboedtuuznum. Pimifo Icmlv Emf DI, Lcdwig owdyzd xwd hce Ywhsmnemzh Xovm mby Cqxtsm Supacg (GUKE) oo Bdmfqclwg Bomk, Tzuhvif'a ocyetzqofifo ositjm. Rcm a lqys ce oie vzav wr Vpt 8, lpq gzclqab mekxabnittq tjr Ymdavn fihog cjgbhvnstkgds. Zm psqikmp o iuejqf jf lmoviiicqg aoj jdsvkavs Uzreiz qdpzmdg, dnutgrdny bts helpar jf lpq pjmtm, mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk naf ohw Mzwbms umqcifm. Mtoej bts raj pq kjrcmp oo tzm Zooigvmz Khqauqvl Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa rcm a kbafzd-hzaumae kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf Zsrmsv'e Qjmhcfwig Dincmalwdm vt Eizqcekbqf Pnadqfnilg, ivzrw pq onsaafsy if bts yenmxckmwvf ca tzm Yoiczmehzr uwydptwze oid tmoohe avfsmekbqr dn eifvzmsbuqvl tqazjgq. Pq kmolm m dvpwz ab ohw ktshiuix pvsaa at hojxtcbefmewn, afl bfzdakfsy okkuzgalqzu xhwuuqvl jmmqoigve gpcz ie hce Tmxcpsgd-Lvvbgbubnkq zqoxtawz, kciup isme xqdgo otaqfqev qz hce 1960k. Bgfdny'a tchokmjivlabk fzsmtfsy if i ofdmavmz krgaqqptawz wi 1952, wzmz vjmgaqlpad iohn wwzq goidt uzgeyix wi tzm Gbdtwl Wwigvwy. Vz aukqdoev bdsvtemzh rilp rshadm tcmmgvqg (xhwuuqvl uiehmalqab) vs sv mzoejvmhdvw ba dmikwz. Hpravs rdev qz 1954, xpsl whsm tow iszkk jqtjrw pug 42id tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl lqhzreqzsy tzif vds vmmhc wsa eidcalq; vds ewfvzr svp gjmw wfvzrk jqzdenmp vds vmmhc wsa mqxivmzhvl. Gv 10 Esktwunsm 2009, fgtxcrifo mb Dnlmdbzt uiydviyv, Nfdtaat Dmiem Ywiikbqf Bojlab Wrgez avdw iz cafakuog pmjxwx ahwxcby gv nscadn at ohw Jdwoikp scqejvysit xwd "hce sxboglavs kvy zm ion tjmmhzd." Sa at Haq 2012 i bfdvsbq azmtmd'g widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo Tmzubb a kbmhptgzk dvrvwz wa efiohzd.""", 'asimov'))


	# print(englishLetterFreqAnalysis('PAEBABANZIAHAKDXAAAKIU'))
	# print(englishLetterFreqAnalysis('OZDAZAZMYHZGZJCWZZZJHT'))
	# print(englishLetterFreqAnalysis('NYCZYZYLXGYFYIBVYYYIGS'))
	# print(englishLetterFreqAnalysis('MXBYXYXKWFXEXHAUXXXHFR'))
	# print(englishLetterFreqAnalysis('LWAXWXWJVEWDWGZTWWWGEQ'))
	# print(englishLetterFreqAnalysis('KVZWVWVIUDVCVFYSVVVFDP'))

	# print(sub.getMostLikleyKeysForLength(4, 'PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU'))
	# 
	sub.makeAllPossibleKeysFromChars([('a','b'), ('c','d')])
