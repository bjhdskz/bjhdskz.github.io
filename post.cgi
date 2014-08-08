#!/usr/bin/perl

$backurl = "http://mtrack.co.in/index.html";
$backname = "admin@mtrack.co.in";
$mailprog = '/usr/sbin/sendmail';
$youmail = 'admin@mtrack.co.in';

read(STDIN, $namevalues, $ENV{'CONTENT_LENGTH'});

open (MAIL, "|$mailprog $youmail") || die "Can't open $mailprog!\n";
print MAIL ("To: $youmail\n");
print MAIL ("From: brupss.com-Contact us\n");
print MAIL ("Subject: from web site\n\n");


@namevalues = split(/&/, $namevalues);
foreach $namevalue (@namevalues) {
($name, $value) = split(/=/, $namevalue);
$name =~ tr/+/ /;
$value =~ tr/+/ /;
$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$INPUT{$name} = $value;
unless ($value eq "") {
print MAIL ("$name: $value\n");
}
}

close (MAIL);


print ("Content-Type: text/html\n\n");
print ("<html><head><title>Thank You</title></head>\n");
print ("<body><h1>Thank You For Filling in the Requested Information</h1>\n");
print ("<hr>\n");
print ("<a href=\"$backurl\">Back to $backname</a><hr>\n");
print ("</body></html>\n");
exit;