!cat https://rcochrane.github.io/markdown_generator/publications.tsv		
import pandas as pd		
publications = pd.read_csv("https://rcochrane.github.io/markdown_generator/publications.tsv", sep="\t", header=0)		
publications		
html_escape_table = {		
     "&": "&amp;",		
     '"': "&quot;",		
     "'": "&apos;"		
     }		

def html_escape(text):		
     """Produce entities within text."""		
     return "".join(html_escape_table.get(c,c) for c in text)		
     import os		
 for row, item in publications.iterrows():		

      md_filename = str(item.pub_date) + "-" + item.url_slug + ".md"		
     html_filename = str(item.pub_date) + "-" + item.url_slug		
     year = item.pub_date[:4]		

      ## YAML variables		

      md = "---\ntitle: \""   + item.title + '"\n'		

      md += """collection: publications"""		

      md += """\npermalink: https://rcochrane.github.io/publications/""" + html_filename		

      if len(str(item.excerpt)) > 5:		
         md += "\nexcerpt: '" + html_escape(item.excerpt) + "'"		

      md += "\ndate: " + str(item.pub_date) 		

      md += "\nvenue: '" + html_escape(item.venue) + "'"		

      if len(str(item.paper_url)) > 5:		
         md += "\npaperurl: '" + item.paper_url + "'"		

      md += "\ncitation: '" + html_escape(item.citation) + "'"		

      md += "\n---"		

      ## Markdown description for individual page		

      if len(str(item.excerpt)) > 5:		
         md += "\n" + html_escape(item.excerpt) + "\n"		

      if len(str(item.paper_url)) > 5:		
         md += "\n[Download paper here](" + item.paper_url + ")\n" 		

      md += "\nRecommended citation: " + item.citation		

      md_filename = os.path.basename(md_filename)		

      with open("https://rcochrane.github.io/_publications/" + md_filename, 'w') as f:		
         f.write(md)  		
 !ls https://rcochrane.github.io/_publications/		
 !cat https://rcochrane/_publications/2019-06-17-Designer-Sinorhizobium-meliloti-strains-and-multi-functional-vectors-enable-direct-inter-kingdom-DNA-transfer.md
