[X, map] = imread("./dark1.jpg");
I = ind2gray(X, map);

J = imadjust(I, [], [], 0.2);

imshowpair(I, J, 'montage')