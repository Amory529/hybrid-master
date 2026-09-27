"""Offline reference implementation. No API calls, no production integration.
Run with Python 3: python3 recombination_reference.py
Allele labels are game rules, not biological claims.
"""
import copy, hashlib, json
from pathlib import Path
HERE=Path(__file__).parent
VERSION='gene-v2-draft-1'
# Each block comes from one parental homolog, preventing broken hair/style-color links.
BLOCKS=[['body_plan','body_scale'],['face_pack'],['body_color'],['surface'],['ear_pack'],['horn_pack'],['hair_pack','hair_color'],['beard_pack'],['headwear'],['eyewear'],['outfit'],['handheld'],['tail'],['wing'],['back'],['glow'],['hand_scale'],['claw'],['limb_color']]
# Explicit directed pair rules; all other pairs use stable, recorded tie-breaking.
DOMINANCE={('body_color',frozenset(['yellow','green'])):'yellow'}
OPTIONAL={'ear_pack','horn_pack','hair_pack','beard_pack','headwear','eyewear','outfit','handheld','tail','wing','back','glow','claw'}
HANDS={'round_stub_feet','round_quadruped','prone_quadruped','banana_upright','penguin_upright','egg_biped'}
TORSO={'round_stub_feet','round_quadruped','prone_quadruped','banana_upright','penguin_upright','egg_biped','round_bust'}
FACE_ANCHORS={
 'heart_blush_tears':['heart pupils','large wet eyes','pink cheek and nose blush','small wavy smile','tear streaks'],
 'sad_frog':['drooping large white eyes','brown thick horizontal lips','under-eye creases'],
 'smirking_dog_blush':['dog nose and muzzle','slight asymmetric smile','rosy cheeks'],
 'bulging_eyes_moustache':['protruding round olive eyes','broad humanlike face'],
 'penguin_beak':['yellow pointed beak','white lower face'],
 'lip_chicken':['high-set large eyes','purple lashes','orange cheeks','turquoise mouth surround','red full lips'],
 'photo_kitten':['forward-facing kitten eyes','small cat nose and mouth','tabby forehead'],
 'dog_big_eyes':['large dark dog eyes','cream short muzzle'],
 'sleepy_pig_snout':['half-closed eyes','short twin-nostril pink snout'],
 'curious_tabby':['yellow green big eyes','pink triangular nose','tabby forehead','cream muzzle'],
 'frowning_bear':['frowning brow','cream broad muzzle','black nose'],
 'black_cat_oval_eyes':['huge oval ivory eyes','black pupils','tiny mouth'],
 'baby_round_eyes':['large round baby eyes','tiny mouth']}
def choice(items,*key):
 digest=hashlib.sha256(json.dumps([VERSION,*key],sort_keys=True).encode()).digest()
 return items[int.from_bytes(digest,'big')%len(items)]
def founder(asset):
 # These are explicit proposed seed genomes, never an inference of hidden DNA.
 values=asset['observed_phenotype']
 return {'id':asset['id'],'seed_policy':'homozygous_observed_proposal','genome':{k:[v,v] for k,v in values.items()}}
def resolve(locus,alleles,seed):
 a,b=alleles
 if a==b:return a,'homozygous'
 if locus in OPTIONAL and 'none' in alleles:return (b if a=='none' else a),'presence_dominant_default'
 win=DOMINANCE.get((locus,frozenset(alleles)))
 if win:return win,'pairwise_dominance'
 return choice(sorted(alleles),seed,'expression',locus),'equal_rank_seeded_choice'
def breed(a,b,seed):
 parents=sorted([a,b],key=lambda p:p['id']);genome={};origins={}
 for block in BLOCKS:
  for parent_i,parent in enumerate(parents):
   homolog=choice([0,1],seed,'meiosis',parent_i,parent['id'],block)
   for locus in block:
    allele=parent['genome'][locus][homolog]
    genome.setdefault(locus,[]).append(allele)
    origins.setdefault(locus,[]).append({'parent':parent['id'],'homolog':homolog})
 selected={};decisions={};trace={}
 for locus,alleles in genome.items():
  selected[locus],decisions[locus]=resolve(locus,alleles,seed)
  trace[locus]=[origins[locus][i]['parent'] for i,v in enumerate(alleles) if v==selected[locus]]
 # Select the hair color from the same transmitted haplotype as the selected hairstyle.
 # Same hairstyle on both homologs can still have independently expressed color variants.
 if genome['hair_pack'][0]!=genome['hair_pack'][1]:
  ix=genome['hair_pack'].index(selected['hair_pack']);selected['hair_color']=genome['hair_color'][ix]
  decisions['hair_color']='linked_to_hair_haplotype';trace['hair_color']=[origins['hair_color'][ix]['parent']]
 expressed=copy.deepcopy(selected);suppressed={}
 def hide(locus,reason):
  if expressed.get(locus)!='none':suppressed[locus]={'allele':expressed[locus],'reason':reason};expressed[locus]='none'
 if expressed['hair_pack']=='none':hide('hair_color','no_hair')
 if expressed['body_plan'] not in HANDS:hide('handheld','no_grasp_anchor')
 if expressed['body_plan'] not in TORSO:hide('outfit','no_torso_adapter')
 if expressed['face_pack']=='heart_blush_tears':hide('eyewear','occludes_heart_eye_identity')
 # Maximum 2 optional high-salience decorations. Core face details never counted here.
 budget=['horn_pack','hair_pack','headwear','eyewear','handheld','back','glow']
 present=[k for k in budget if expressed[k]!='none']
 priority=sorted(present,key=lambda k:hashlib.sha256(f'{VERSION}/{seed}/budget/{k}'.encode()).hexdigest())
 for k in priority[2:]:hide(k,'salience_budget')
 if expressed['hair_pack']=='none':hide('hair_color','hair_suppressed')
 # All suppression leaves the inherited genome untouched.
 primary=choice(trace['body_plan'],seed,'primary');visible_signature=[k for k in ['face_pack','hair_pack','beard_pack','headwear','eyewear','handheld','ear_pack','horn_pack','tail','wing'] if expressed[k]!='none' and any(p!=primary for p in trace[k]) and parents[0]['genome'][k]!=parents[1]['genome'][k]]
 anchors=FACE_ANCHORS.get(expressed['face_pack'],[])
 brief={'body_plan':expressed['body_plan'],'face_anchors':anchors,'phenotype':expressed,'salience_limit':2,'triangle_target':4500,'triangle_hard_cap':7000,'must_not':['extra heads','split half-parent bodies','floating facial parts'],'review_required':True}
 return {'id':hashlib.sha256(f'{parents[0]["id"]}/{parents[1]["id"]}/{seed}/{VERSION}'.encode()).hexdigest()[:16],'version':VERSION,'seed':seed,'parents':[p['id'] for p in parents],'genome':genome,'inherited_allele_sources':origins,'expression_decisions':decisions,'selected_before_constraints':selected,'phenotype':expressed,'suppressed':suppressed,'primary_parent':primary,'visible_secondary_signature_loci':visible_signature,'status':'ready_for_reference_review' if visible_signature else 'needs_review_no_visible_second_parent','brief':brief}
def main():
 assets=json.loads((HERE/'gene_assets_v2.json').read_text())['assets'];parents={a['id']:founder(a) for a in assets}
 examples=[breed(parents[a],parents[b],17) for a,b in [('heart-emoji','sad-frog'),('knife-dog','fengge'),('gentle-penguin','curious-cat')]]
 # Tests that matter: inheritance, repeatability, parent-order independence,
 # recessive recovery, block linkage, suppressed carrier retention.
 a=parents['heart-emoji'];b=parents['sad-frog']
 assert breed(a,b,17)==breed(a,b,17)==breed(b,a,17)
 for ex in examples:
  pa,pb=[parents[x] for x in ex['parents']]
  for k,values in ex['genome'].items():assert values[0] in pa['genome'][k] and values[1] in pb['genome'][k]
  for k,v in ex['suppressed'].items():assert v['allele'] in ex['genome'][k]
 f1=breed(a,b,1);assert f1['selected_before_constraints']['body_color']=='yellow'
 f1a=copy.deepcopy(f1);f1a['id']='sibling-a';f1b=copy.deepcopy(f1);f1b['id']='sibling-b'
 counts={'yellow':0,'green':0}
 for seed in range(4096):counts[breed(f1a,f1b,seed)['selected_before_constraints']['body_color']]+=1
 assert .22 < counts['green']/4096 < .28
 # Every optional allele may be hidden but never erased by expression constraints.
 sph=copy.deepcopy(a);sph['genome']['handheld']=['knife_shield']*2
 ex=breed(sph,sph,3);assert ex['phenotype']['handheld']=='none' and ex['genome']['handheld']==['knife_shield']*2
 report={'status':'passed','sample_size':4096,'F2_color_counts':counts,'tests':['same seed deterministic','parent order independent','one inherited allele per parent','hidden allele retained','F2 recessive reappearance','sphere suppresses handheld without deleting it'],'scope':'offline reference genetics only; visual similarity and Tripo integration untested'}
 (HERE/'offspring_examples.json').write_text(json.dumps(examples,ensure_ascii=False,indent=2))
 (HERE/'simulation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':main()
