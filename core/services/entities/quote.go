package entities

type Quote struct {
	Base
	Quote string `gorm:"column:quote;size:512;not null;<-;"`
}
