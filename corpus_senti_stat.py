#!/usr/bin/python
# -*- coding: utf-8 -*-


#<document doc_id="1" title="unknown">
#<p>
#<s>
#Das	T-dnsn-	die	NULL	NULL	SUBJ_EMB	1	2	NK	ART.Def.Nom.Sg.Neut	NULL	NULL	NULL	NULL	NULL
#Buch	Ncnsn	Buch	NULL	NULL	SUBJ_HD,SUBJ_EMB	1,1	3	SB	N.Reg.Nom.Sg.Neut	NULL	NULL	NULL	NEUT;1	NULL
#ist	Vaip3s-	sein	NULL	NULL	V_O_A	1	0	--	VFIN.Aux.3.Sg.Pres.Ind	NULL	NEG;0.289392/0.465159/0.24545	NULL	NULL	NULL
#sehr	R--	sehr	NULL	NULL	NULL	NULL	5	MO	ADV	NULL	POS;0.350257/0.388175/0.261568	NULL	NULL	NULL
#sehr	R--	sehr	NULL	NULL	NULL	NULL	6	MO	ADV	NULL	POS;0.350257/0.388175/0.261568	NULL	NULL	NULL
#traurig	R--	traurig	NULL	NULL	PRED_ADJ	1	3	PD	ADJD.Pos	NULL	NEG;-/-0.1266/-	neg	NEG;1	NEG;-0.1266
#,	S	,	NULL	NULL	NULL	NULL	6	--	SYM.Pun.Comma	NULL	NULL	NULL	NULL	NULL
#aber	Cc	aber	NULL	NULL	NULL	NULL	6	CD	CONJ.Coord	NULL	NEUT;0.251292/0.469234/0.279474	NULL	NULL	NULL
#auch	R--	auch	NULL	NULL	NULL	NULL	12	MO	ADV	NULL	NEUT;0.318928/0.434745/0.246327	NULL	NULL	NULL
#irgendwie	R--	irgendwie	NULL	NULL	NULL	NULL	12	MO	ADV	NULL	NULL	NULL	NULL	NULL
#sehr	R--	sehr	NULL	NULL	NULL	NULL	12	MO	ADV	NULL	POS;0.350257/0.388175/0.261568	NULL	NULL	NULL
#schön	R--	schön	NULL	NULL	NULL	NULL	8	CJ	ADJD.Pos	NULL	POS;0.0081/-/-	pos	POS;1	POS;0.0081
#und	Cc	und	NULL	NULL	NULL	NULL	3	CD	CONJ.Coord	NULL	NULL	NULL	NULL	NULL
#man	Pi--sn-	man	LC.WF	LC.FALSE	SUBJ_HD,SUBJ_EMB	2,2	15	SB	PRO.Indef.Subst.Nom.Sg.*	NULL	NULL	NULL	NULL	NULL
#möchte	Voss3s-	mögen	NULL	NULL	NULL	NULL	13	CJ	VFIN.Mod.3.Sg.Past.Subj	NULL	POS;0.345/-/-	pos	POS;1	POS;0.345
#auch	R--	auch	NULL	NULL	NULL	NULL	15	MO	ADV	NULL	NEUT;0.318928/0.434745/0.246327	NULL	NULL	NULL
#einfach	R--	einfach	NULL	NULL	NULL	NULL	18	MO	ADV	NULL	POS;0.0040/-/-	NULL	POS;0.7	POS;0.0040
#wissen	Vmn-----	wissen	LC.SIM_GROUP	LC.FALSE	V_M_A	2	15	OC	VINF.Full	NULL	NULL	NULL	NULL	NULL
#wie	Cv	wie	NULL	NULL	NULL	NULL	21	CM	CONJ.Comp	NULL	NULL	NULL	NULL	NULL
#dieses	Pd-nsa-	dieses	LC.WF	LC.FALSE	NULL	NULL	21	NK	PRO.Dem.Attr.Acc.Sg.Neut	NULL	NULL	NULL	NULL	NULL
#Buch	Ncnsa	Buch	NULL	NULL	NULL	NULL	22	MO	N.Reg.Acc.Sg.Neut	NULL	NULL	NULL	NEUT;1	NULL
#endet	Vmip3s-	enden	NULL	NULL	V_O_A	3	18	OC	VFIN.Full.3.Sg.Pres.Ind	000	NULL	NULL	NULL	NULL
#.	S	.	NULL	NULL	NULL	NULL	22	--	SYM.Pun.Sent	NULL	NEUT;0.281739/0.473789/0.244472	NULL	NULL	NULL
#</s>
#<s>
#Also	R--	also	NULL	NULL	SUBJ_EMB	4	2	MO	ADV	NULL	NULL	NULL	NULL	NULL
#ich	Pp1-sn-	sie	NULL	NULL	SUBJ_HD,SUBJ_EMB	4,4	3	SB	PRO.Pers.Subst.1.Nom.Sg.*	NULL	NULL	NULL	NULL	NULL
#konnte	Vois1s-	können	NULL	NULL	NULL	NULL	0	--	VFIN.Mod.1.Sg.Past.Ind	NULL	NEUT;0.331807/0.440712/0.227481	NULL	NULL	NULL
#das	Pd-nsa-	das	LC.WF	LC.FALSE	OBJ_HD,OBJ_EMB	4,4	10	OA	PRO.Dem.Subst.Acc.Sg.Neut	NULL	NULL	NULL	NULL	NULL
#nicht	Qn	nicht	NULL	NULL	NEG	4	3	NG	PART.Neg	NULL	NEG;0.25515/0.49701/0.247841	NULL	NULL	NULL
#wieder	R--	wieder	NULL	NULL	NULL	NULL	10	MO	ADV	NULL	NULL	NULL	NULL	NULL
#aus	Sp-	aus	NULL	NULL	APP_HD,APP_EMB	4,4	10	MO	APPR	NULL	NEG;0.302227/0.486744/0.211029	NULL	NULL	NULL
#der	T-dfsd-	die	NULL	NULL	APP_EMB	4	9	NK	ART.Def.Dat.Sg.Fem	NULL	NULL	NULL	NULL	NULL
#Hand	Ncfsd	Hand	NULL	NULL	APP_EMB	4	7	NK	N.Reg.Dat.Sg.Fem	NULL	NULL	NULL	NEUT;1	NULL
#legen	Vmn-----	legen	LC.SIM_GROUP	LC.FALSE	V_M_A	4	3	OC	VINF.Full	000	NEUT;0.322222/0.455556/0.222222	NULL	NULL	NULL
#.	S	.	NULL	NULL	NULL	NULL	10	--	SYM.Pun.Sent	NULL	NEUT;0.281739/0.473789/0.244472	NULL	NULL	NULL
#</s>
#</p>
#</document>

# top ten most positiv reviews (review is something between document<>, count "positives" inwithin those documents, sentence barrier not count),
# sentiments are the following rows: 11-  12-  13- 14-
# outwrite information by eaxh lexica (only taking into account row 11, or only row 12 or only row 13 etc.)
# outwrite information taking into account all the rows. Count +1 if there is a positive value at least at one of the rows.
# outwrite number of a review (hidden in doc_id  + sorted from the review with the highest numeber to the least number. + print the top 10 reviews)

# the same for the negatives.

# the same for the weights. Combine the weights: see row 11, row 13. Here count only separates.

# find the most often used positive and negative, neutral words.
# ourwrite all positive and negative words. Should count as positive or negative if at least on of the rows 11, 12, 13, 14 has a sentiment.