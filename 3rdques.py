x = {'hello': ['doc1'], 'my': ['doc1'], 'name': ['doc1'], 'is': ['doc1', 'doc2'], 'james': ['doc1', 'doc2'],
'a': ['doc2'], 'developer': ['doc2']}

val1={k: v for k, v in x.items() if len(v)==1}
val2={k: v for k, v in x.items() if len(v)==2}
key_sort1= {k: v for k, v in sorted(val1.items(), key=lambda item: len(item[0]))}
key_sort2={k: v for k,v in sorted(val2.items(),key=lambda item: len(item[0]))}

print({**key_sort1,**key_sort2})
