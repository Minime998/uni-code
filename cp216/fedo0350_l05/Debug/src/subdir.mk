################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/main.c \
../src/name_list.c \
../src/rm_library.c 

C_DEPS += \
./src/main.d \
./src/name_list.d \
./src/rm_library.d 

OBJS += \
./src/main.o \
./src/name_list.o \
./src/rm_library.o 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c src/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: Cygwin C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-src

clean-src:
	-$(RM) ./src/main.d ./src/main.o ./src/name_list.d ./src/name_list.o ./src/rm_library.d ./src/rm_library.o

.PHONY: clean-src

