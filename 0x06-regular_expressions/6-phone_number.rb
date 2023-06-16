#!/usr/bin/env ruby
puts ARGV[0].scan(/^\d{10}$/).join # same as ([0-9]{10})
