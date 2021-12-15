import smbus
# AD0=L にした場合は MPU-9250（加速度,ジャイロ部）のスレーブアドレスが 0b1101000 = 0x68
ADDRESS = 0b1101000
i2c = smbus.SMBus(1)
#  0x75(WHO_AM_I)を読んで 0x71が読めれば正常です。
who_am_i = i2c.read_byte_data(ADDRESS, 0x75)
print(  hex(who_am_i ) )

# 内部アドレス 0x6Bに 0x00を書き込みます。
i2c.write_byte_data( ADDRESS, 0x6b, 0x00 )

# さらに内部アドレス 0x37に 0x02を書き込みます。
i2c.write_byte_data( ADDRESS, 0x37, 0x02 )

# 0x3Bからの 14バイトに加速度 X,Y,Z, ジャイロ X,Y,Zのデータが入ります。
acc_x_lsb = i2c.read_byte_data( ADDRESS, 0x3B )
acc_x_msb = i2c.read_byte_data( ADDRESS, 0x3B+1 )
acc_y_lsb = i2c.read_byte_data( ADDRESS, 0x3B+2 )
acc_y_msb = i2c.read_byte_data( ADDRESS, 0x3B+3 )
acc_z_lsb = i2c.read_byte_data( ADDRESS, 0x3B+4 )
acc_z_msb = i2c.read_byte_data( ADDRESS, 0x3B+5 )

gyr_x_lsb = i2c.read_byte_data( ADDRESS, 0x3B+6 )
gyr_x_msb = i2c.read_byte_data( ADDRESS, 0x3B+7 )
gyr_y_lsb = i2c.read_byte_data( ADDRESS, 0x3B+8 )
gyr_y_msb = i2c.read_byte_data( ADDRESS, 0x3B+9 )
gyr_z_lsb = i2c.read_byte_data( ADDRESS, 0x3B+10 )
gyr_z_msb = i2c.read_byte_data( ADDRESS, 0x3B+11 )

print([acc_x_lsb,acc_x_msb,acc_y_lsb,acc_y_msb,acc_z_lsb,acc_z_msb])
print([gyr_x_lsb,gyr_x_msb,gyr_y_lsb,gyr_y_msb,gyr_z_lsb,gyr_z_msb])

i2c.close()