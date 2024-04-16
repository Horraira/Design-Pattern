package com.packg;
// a real text calculator for the year 2024 that implements the TaxCalculator interface
public class TaxCalculator2024 implements TaxCalculator{
    @Override
    public float calculateTax() {
        return 1;
    }

    // this method is not part of the TaxCalculator interface
    public float calculateInsurance(){
        return 0;
    }
}
