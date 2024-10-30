package com.rubypaper.service;

import java.time.LocalDate;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.rubypaper.dto.Calendar;
import com.rubypaper.dto.Meal;
import com.rubypaper.jpa.CalendarRepository;

@Service
public class CalendarService {
	@Autowired
    private CalendarRepository calendarRepository;
    
	// 특정 월의 모든 식사 데이터를 반환
    public List<Calendar> getCalendarsByMonth(String userId, int year, int month) {
        LocalDate startDate = LocalDate.of(year, month, 1);
        LocalDate endDate = startDate.withDayOfMonth(startDate.lengthOfMonth());
        return calendarRepository.findByUserIdAndSaveDateBetween(userId, startDate, endDate);
    }
    
    // 특정 userId에 해당하는 캘린더 항목 리스트를 반환
    public Calendar getCalendarsByUserIdAndSaveDate(String userId, LocalDate saveDate) {
        return calendarRepository.findByUserIdAndSaveDate(userId, saveDate).orElse(null);
    }
    
    // 수정 calendar 정보 저장
    public void saveCalendar(Calendar calendar, List<String> foods) {
    	String breakfast = foods.get(0);
        String lunch = foods.get(1);
        String dinner = foods.get(2);
    	
    	calendar.setBreakfast(breakfast);
    	calendar.setLunch(lunch);
    	calendar.setDinner(dinner);
    	
    	calendarRepository.save(calendar);
    }
    
    public void deleteCalendar(String userId, LocalDate date) {
        Calendar calendar = calendarRepository.findByUserIdAndSaveDate(userId, date).orElse(null);
        if (calendar != null) {
            calendarRepository.delete(calendar);
        }
    }
}
