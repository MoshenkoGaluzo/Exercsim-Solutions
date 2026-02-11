public class JedliksToyCar {

    private int meters = 0;
    private int battery = 100;
    
    public static JedliksToyCar buy() {
        return new JedliksToyCar();
    }

    public String distanceDisplay() {
        return "Driven " + meters + " meters";
    }

    public String batteryDisplay() {
        if(battery > 0){
            return "Battery at " + battery + "%";
        }
        else{
            return "Battery empty";
        }
    }

    public void drive() {
        if(battery > 0){
            meters += 20;
            battery--;
        }
    }
}
