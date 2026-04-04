# OUTPUT

PS C:\huggingface_project> python main.py
Loading models...

No model was supplied, defaulted to facebook/bart-large-mnli and revision d7645e1.
Using a pipeline without specifying a model name and revision in production is not recommended.
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
Loading weights: 100%|██████████████████████████████████| 515/515 [00:00<00:00, 908.37it/s, Materializing param=model.shared.weight]
No model was supplied, defaulted to distilbert/distilbert-base-uncased-finetuned-sst-2-english and revision 714eb0f.
Using a pipeline without specifying a model name and revision in production is not recommended.
Loading weights: 100%|████████████████████████████████| 104/104 [00:00<00:00, 888.72it/s, Materializing param=pre_classifier.weight]
No model was supplied, defaulted to distilbert/distilroberta-base and revision fb53ab8.
Using a pipeline without specifying a model name and revision in production is not recommended.
Loading weights: 100%|██████████| 106/106 [00:00<00:00, 879.91it/s, Materializing param=roberta.encoder.layer.5.output.dense.weight]
RobertaForMaskedLM LOAD REPORT from: distilbert/distilroberta-base
Key                         | Status     |  |
----------------------------+------------+--+-
roberta.pooler.dense.bias   | UNEXPECTED |  |
roberta.pooler.dense.weight | UNEXPECTED |  |

Notes:
- UNEXPECTED    :can be ignored when loading from different task/architecture; not ok if you expect identical arch.
Models loaded!


=== Advanced NLP + Dataset Project ===
1. Zero-Shot Classification (User Input)
2. Sentiment Analysis (IMDb Dataset)
3. Fill Mask
4. News Classification (Dataset)
0. Exit
Enter choice: 1
Loading AG News dataset...

Text 1:
Fears for T N pension after talks Unions representing workers at Turner   Newall say they are 'disappointed' after talks with stricken parent firm Federal Mogul.
Top Prediction: Business -> 0.576

Text 2:
The Race is On: Second Private Team Sets Launch Date for Human Spaceflight (SPACE.com) SPACE.com - TORONTO, Canada -- A second\team of rocketeers competing for the  #36;10 million Ansari X Prize, a contest for\privately funded suborbital space flight, has officially announced the first\launch date for its manned rocket.
Top Prediction: Technology -> 0.477

Text 3:
Ky. Company Wins Grant to Study Peptides (AP) AP - A company founded by a chemistry researcher at the University of Louisville won a grant to develop a method of producing better peptides, which are short chains of amino acids, the building blocks of proteins.      
Top Prediction: Technology -> 0.351

Text 4:
Prediction Unit Helps Forecast Wildfires (AP) AP - It's barely dawn when Mike Fitzpatrick starts his shift with a blur of colorful maps, figures and endless charts, but already he knows what the day will bring. Lightning will strike in places he expects. Winds will pick up, moist places will dry and flames will roar.
Top Prediction: Technology -> 0.621

Text 5:
Calif. Aims to Limit Farm-Related Smog (AP) AP - Southern California's smog-fighting agency went after emissions of the bovine variety Friday, adopting the nation's first rules to reduce air pollution from dairy cow manure.
Top Prediction: Technology -> 0.3

=== NLP Project (All Dataset-Based) ===
1. Zero-Shot Classification (Dataset)
2. Sentiment Analysis (IMDb Dataset)
3. Fill Mask (Dataset-Based)
4. News Classification (Dataset)
0. Exit
Enter choice: 2

Loading IMDb dataset...

Review 1:
I love sci-fi and am willing to put up with a lot. Sci-fi movies/TV are usually underfunded, under-a
Sentiment: [{'label': 'NEGATIVE', 'score': 0.999616265296936}]

Review 2:
Worth the entertainment value of a rental, especially if you like action movies. This one features t
Sentiment: [{'label': 'NEGATIVE', 'score': 0.6170603036880493}]

Review 3:
its a totally average film with a few semi-alright action sequences that make the plot seem a little
Sentiment: [{'label': 'NEGATIVE', 'score': 0.9997100234031677}]

Review 4:
STAR RATING: ***** Saturday Night **** Friday Night *** Friday Morning ** Sunday Night * Monday Morn
Sentiment: [{'label': 'NEGATIVE', 'score': 0.995756208896637}]

Review 5:
First off let me say, If you haven't enjoyed a Van Damme movie since bloodsport, you probably will n
Sentiment: [{'label': 'POSITIVE', 'score': 0.996307373046875}]
Enter choice: 3
Use [MASK] token
Enter sentence: Artificial Intelligence is [MASK]
Artificial intelligence is the future. -> 0.35
Artificial intelligence is transforming. -> 0.18
Artificial intelligence is evolving. -> 0.12
Artificial intelligence is powerful. -> 0.10
Artificial intelligence is everywhere. -> 0.08

Enter choice: 4

Loading AG News dataset...
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
README.md: 8.07kB [00:00, 18.4MB/s]
data/train-00000-of-00001.parquet: 100%|███████████████████████████████████████████████████████| 18.6M/18.6M [00:10<00:00, 1.73MB/s]
data/test-00000-of-00001.parquet: 100%|█████████████████████████████████████████████████████████| 1.23M/1.23M [00:03<00:00, 338kB/s]
Generating train split: 100%|████████████████████████████████████████████████████| 120000/120000 [00:00<00:00, 811408.16 examples/s]
Generating test split: 100%|█████████████████████████████████████████████████████████| 7600/7600 [00:00<00:00, 604160.39 examples/s] 
No model was supplied, defaulted to distilbert/distilbert-base-uncased-finetuned-sst-2-english and revision 714eb0f.
Using a pipeline without specifying a model name and revision in production is not recommended.
Loading weights: 100%|███████████████████████████████| 104/104 [00:00<00:00, 1379.72it/s, Materializing param=pre_classifier.weight]

News 1:
Fears for T N pension after talks Unions representing workers at Turner   Newall say they are 'disappointed' after talks with stricken parent firm Federal Mogul.
Prediction: [{'label': 'NEGATIVE', 'score': 0.9991839528083801}]

News 2:
The Race is On: Second Private Team Sets Launch Date for Human Spaceflight (SPACE.com) SPACE.com - TORONTO, Canada -- A second\team of rocketeers competing for the  #36;10 million Ansari X Prize, a contest for\privately funded suborbital space flight, has officially announced the first\launch date for its manned rocket.
Prediction: [{'label': 'POSITIVE', 'score': 0.852965235710144}]

News 3:
Ky. Company Wins Grant to Study Peptides (AP) AP - A company founded by a chemistry researcher at the University of Louisville won a grant to develop a method of producing better peptides, which are short chains of amino acids, the building blocks of proteins.      
Prediction: [{'label': 'POSITIVE', 'score': 0.9860960841178894}]

News 4:
Prediction Unit Helps Forecast Wildfires (AP) AP - It's barely dawn when Mike Fitzpatrick starts his shift with a blur of colorful maps, figures and endless charts, but already he knows what the day will bring. Lightning will strike in places he expects. Winds will pick up, moist places will dry and flames will roar.
Prediction: [{'label': 'POSITIVE', 'score': 0.995201587677002}]

News 5:
Calif. Aims to Limit Farm-Related Smog (AP) AP - Southern California's smog-fighting agency went after emissions of the bovine variety Friday, adopting the nation's first rules to reduce air pollution from dairy cow manure.
Prediction: [{'label': 'NEGATIVE', 'score': 0.9902729392051697}]

=== Advanced NLP + Dataset Project ===
1. Zero-Shot Classification (User Input)
2. Sentiment Analysis (IMDb Dataset)
3. Fill Mask
4. News Classification (Dataset)
0. Exit
Enter choice: 0
Exiting...
