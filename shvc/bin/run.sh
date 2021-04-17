time ./TAppEncoderStatic -c ../cfg/encoder_randomaccess_scalable.cfg -c ../cfg/layers.cfg -c ../cfg/per-sequence-svc/akio-layers2.cfg
mv str.bin layers2.bin
time ./TAppEncoderStatic -c ../cfg/encoder_randomaccess_scalable.cfg -c ../cfg/threelayers.cfg -c ../cfg/per-sequence-svc/akio-layers3.cfg
mv str.bin layers3.bin
time ./TAppEncoderStatic -c ../cfg/encoder_randomaccess_scalable.cfg -c ../cfg/fourlayers.cfg -c ../cfg/per-sequence-svc/akio-layers4.cfg
mv str.bin layers4.bin
time ./TAppEncoderStatic -c ../cfg/encoder_randomaccess_scalable.cfg -c ../cfg/fivelayers.cfg -c ../cfg/per-sequence-svc/akio-layers5.cfg
mv str.bin layers5.bin
time ./TAppEncoderStatic -c ../cfg/encoder_randomaccess_scalable.cfg -c ../cfg/sixlayers.cfg -c ../cfg/per-sequence-svc/akio-layers6.cfg
mv str.bin layers6.bin
