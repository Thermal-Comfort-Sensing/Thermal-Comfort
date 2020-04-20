
function drawAngleData(csvFileName)

% angle1, angle2, temperature
data1 = csvread(csvFileName);
figure;
subplot(3,1,1);
drawNaive(data1);
subplot(3,1,2);
drawSphere(data1,false);
axis square;
view(105,5);
subplot(3,1,3);
drawSphere(data1,true);
view(-90,0);
end


function drawNaive(csvData)
% very naive method: ignore distortion and treat angles as linear points
% the data is square
imgSize = sqrt(size(csvData));
asLinear = flipud(reshape(csvData(:,3), imgSize(1), imgSize(1))');
imagesc(asLinear)
end

function drawSphere(csvData, flatten)
% technically correct, but hard to use
% the data is square
imgSize = sqrt(size(csvData));
asBlock = reshape(csvData, imgSize(1), imgSize(1), 3);
thetas = asBlock(:,:,1);
phis = asBlock(:,:,2);
temps = asBlock(:,:,3);

% the image can be drawn from y,z if you want it in 2 dimensions
if flatten
  xs = ones(imgSize(1));
else
  xs = cos(thetas).*cos(phis);
end
ys = cos(thetas).*sin(phis);
zs = sin(thetas);

% map all temperatures between 0 and 1
tempMapping = (temps-min(temps(:)))./(max(temps(:))-min(temps(:)));
% grayscale must be repeated for r,g,b
tempColors = repmat(tempMapping,1,1,3);

surf(xs,ys,zs, tempColors, 'EdgeColor','none');
end
