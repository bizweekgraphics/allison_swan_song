import collections
import csv

c = collections.Counter()
with open('movies_all.txt', 'rt') as f:
    for line in f:
        c.update(line.split())

print 'the most common words are:'
for words, count in c.most_common(150):
    print '%s: %7d' % (words, count)

#if __name__ == '__main__':                              # __name__ is the name of the "current" file                                      #thats always the filename unless im executing directly (i.e. python imdb.py)
 #   with open('movies_count.csv', 'w') as output:      # in wihch case __name__ will be "__main__". This helps with importing.
  #      csvwriter = csv.writer(output)                  # this is beautiful soup way of writing to a CSV
   #     for words in f:
    #        keywords = words
     #       count = count                 # at first i tried 'http://www.imdb.com' + url + 'keywords/' which worked but .format is cleaner
      #      csvwriter.writerow([keywords, count])
       # if UnicodeEncodeError: #ugh unicode errors will follow you to your grave
        #    pass 
