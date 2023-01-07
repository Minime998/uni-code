package lesson04;

public interface OperateTV {
	// constant declarations, if any
	// method signatures
	// An enum with values UP, Down
	int turnOn();

	int turnOff();

	int increaseVolume(double value);

	int decreaseVolume(double valu);

	int changeChannel(int chanelNumber);

	int pressTVMenu();
	// more method signatures
}
