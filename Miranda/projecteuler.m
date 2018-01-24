%starting out the fibonacci sequence
f1=1;
f2=2;

wholeFib=zeros(1,1); %initialising a matrix for the whole sequence
wholeFib(1)=f1
wholeFib(2)=f2

%finding the fibonacci sequence
c=1; %setting an arbitrary counter
for i=3:(34-2)
    fibSequence=wholeFib(c)+wholeFib(c+1); 
    wholeFib(i)=fibSequence; %putting each new element into the matrix
    c=c+1;
end
wholeFib

evenFib=zeros(1,1); %setting up a matrix for just the even #
d=1; %arbitrary counter so nothing gets overwritten in the matrix except 0
for i=1:32
    if rem(wholeFib(i),2)==0 %for even numbers
        evenFib(d)=wholeFib(i); %referring to the wholeFib(i) that you've vetted with the rem
        d=d+1;
    end
end
evenFib

%doing a sum loop
%setting up variables to sum stuff
aSum=0;
totalSum=0;
for i=1:2:10
    aSum=evenFib(i)+evenFib(i+1);
    totalSum=aSum+totalSum;
end
totalSum=totalSum+evenFib(11); %cannot make i go larger than 10 because there are only 11 elements in the matrix and you need an i+1
totalSum
    
    