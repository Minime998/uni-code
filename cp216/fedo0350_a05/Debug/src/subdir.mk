################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/myrecord_sllist.c \
../src/myrecord_sllist_main.c 

C_DEPS += \
./src/myrecord_sllist.d \
./src/myrecord_sllist_main.d 

OBJS += \
./src/myrecord_sllist.o \
./src/myrecord_sllist_main.o 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: Cygwin C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-src

clean-src:
	-$(RM) ./src/myrecord_sllist.d ./src/myrecord_sllist.o ./src/myrecord_sllist_main.d ./src/myrecord_sllist_main.o

.PHONY: clean-src

