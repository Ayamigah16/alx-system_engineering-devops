#!/usr/bin/env ruby

# Search for "hbt" followed by one or more
# "n" characters and print the result.
puts ARGV[0].scan(/hbt+n/).join
